# ao3-project

This repository stores large CSV data files using Git LFS. To fetch the CSV files after cloning (or if they are missing locally), follow these steps.

1) Install Git LFS

	- On Debian/Ubuntu: sudo apt-get install git-lfs
	- macOS (Homebrew): brew install git-lfs
	- Or download from https://git-lfs.github.com

2) Clone the repo (if you haven't already)

	git clone https://github.com/vchinni006/ao3-project.git

3) Enable Git LFS and fetch LFS objects

	cd ao3-project
	git lfs install
	git lfs pull

4) Verify the files exist

	ls -lh tags-20210226.csv tags_cleaned.csv works-20210226.csv

Notes:
- Git LFS stores large files outside of regular git objects; you must have Git LFS installed to download the actual CSV contents.
- GitHub may enforce storage/bandwidth limits for LFS objects on your account or organization.

```
# ao3-project
