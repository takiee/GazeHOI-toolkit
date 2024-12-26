# Gaze-guided Hand-Object Interaction Synthesis: Dataset and Method
![](doc/teaser.png)
[paper](https://arxiv.org/abs/2403.16169) |
[video](https://www.youtube.com/watch?v=BR9qkQQpUfg) | 
[project page](https://takiee.github.io/gaze-hoi/)
## Dataset
![](doc/dataset.png)
Download link: [GoogleDrive](https://drive.google.com/drive/folders/1_3i8Pw_GLx4lDmULPVxJMWNG8fTa2rzY?usp=drive_link)
### Data Structure
```
release_data/
├── 0001/
│   ├── mano/
│   │   ├── poses_left.npy 
│   │   └── poses_right.npy 
│   ├── 001_book_4_pose_trans.npy
│   ├── 007_pen_3_blue_pose_trans.npy
│   ├── 007_pen_4_green_pose_trans.npy
│   ├── 007_pen_5_orange_pose_trans.npy
│   ├── ego_calib.npy
│   ├── gaze.npy # gaze ray
│   ├── gaze_point.npy
│   └── meta.pkl # Metadata, including active object labels, hand flags, and other details.
├── 0002/
│   ├── ...
└── ...
```

### Load Data
```
python scripts/read_data.py --seq_id 1
```

## Citation
If you find our work useful in your research, please consider citing:

```
@misc{GazeHOI,
      title={Gaze-guided Hand-Object Interaction Synthesis: Dataset and Method}, 
      author={Jie Tian and Ran Ji and Lingxiao Yang and Suting Ni and Yuexin Ma and Lan Xu and Jingyi Yu and Ye Shi and Jingya Wang},
      year={2024},
      eprint={2403.16169},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2403.16169}, 
}
```
