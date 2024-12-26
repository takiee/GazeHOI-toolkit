import numpy as np 
import os
from os.path import join
import pickle
import trimesh
import argparse
from manotorch.manolayer import ManoLayer
import torch

path = './release_data/'
obj_root = './release_obj/'
parser = argparse.ArgumentParser(description="Read data for a specific sequence ID.")
parser.add_argument('--seq_id', type=int, required=True, help="Sequence ID to read data for.")
args = parser.parse_args()
seq = str(args.seq_id).zfill(4)

seq_path = join(path,seq)

# meta data
with open(join(seq_path,'info.pkl'),'rb')as f:
    meta = pickle.load(f)
print(meta)

# object data
active_obj = meta['active_obj']
obj_path = join(obj_root,active_obj,'simplified_scan_processed.obj')
obj_mesh = trimesh.load(obj_path)
obj_verts = obj_mesh.vertices
obj_faces = obj_mesh.faces
obj_pose = np.load(join(seq_path,active_obj+'_pose_trans.npy'))
print(obj_verts.shape)
print(obj_faces.shape)
print(obj_pose.shape)


# hand data
left_manolayer = ManoLayer(mano_assets_root='./mano',side='left')
right_manolayer = ManoLayer(mano_assets_root='./mano',side='right')

left_hand_faces = left_manolayer.th_faces
right_hand_faces = right_manolayer.th_faces

left_params = torch.tensor(np.load(join(seq_path,'mano/poses_left.npy')))
right_params = torch.tensor(np.load(join(seq_path,'mano/poses_right.npy')))


left_trans = left_params[:,:3]
left_theta = left_params[:,3:51]
left_beta = left_params[:,51:]
left_output = left_manolayer(left_theta, left_beta)
left_verts = left_output.verts - left_output.joints[:, 0].unsqueeze(1) + left_trans.unsqueeze(1)
left_joints = left_output.joints - left_output.joints[:, 0].unsqueeze(1) + left_trans.unsqueeze(1)
print(left_params.shape)
print(left_joints.shape)
print(left_verts.shape)


right_trans = right_params[:,:3]
right_theta = right_params[:,3:51]
right_beta = right_params[:,51:]
right_output = right_manolayer(right_theta, right_beta)
right_verts = right_output.verts - right_output.joints[:, 0].unsqueeze(1) + right_trans.unsqueeze(1)
right_joints = right_output.joints - right_output.joints[:, 0].unsqueeze(1) + right_trans.unsqueeze(1)
print(right_params.shape)
print(right_joints.shape)
print(right_verts.shape)

# gaze data
gaze_ray = np.load(join(seq_path,'gaze.npy'))
gaze_point = np.load(join(seq_path,'gaze_point.npy'))
print(gaze_ray.shape)
print(gaze_point.shape)