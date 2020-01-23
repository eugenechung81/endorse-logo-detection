
## 1.1 Installation of Open CV using source 

Following instructions from: https://www.pyimagesearch.com/2018/05/28/ubuntu-18-04-how-to-install-opencv/.
NOTE: Does not work with python3.7. 

```bash
sudo apt-get install build-essential cmake unzip pkg-config
sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libatlas-base-dev gfortran
sudo apt-get install python3-dev

cd ~
wget -O opencv.zip https://github.com/opencv/opencv/archive/3.4.4.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/3.4.4.zip
unzip opencv.zip
unzip opencv_contrib.zip
mv opencv-3.4.4 opencv
mv opencv_contrib-3.4.4 opencv_contrib

wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py
sudo pip install virtualenv virtualenvwrapper
sudo rm -rf ~/get-pip.py ~/.cache/pip

mkvirtualenv cv -p python3
cd opencv
mkdir build 
cmake -D CMAKE_BUILD_TYPE=RELEASE \\n\t-D CMAKE_INSTALL_PREFIX=/usr/local \\n\t-D INSTALL_PYTHON_EXAMPLES=ON \\n\t-D INSTALL_C_EXAMPLES=OFF \\n\t-D OPENCV_ENABLE_NONFREE=ON \\n\t-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \\n\t-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \\n\t-D BUILD_EXAMPLES=ON ..
make -j4

sudo make install

```

## 1.2 Fix 

Install matploblib with TkAgg dependencies

```
pip unstinall matplotlib
git clone https://github.com/matplotlib/matplotlib.git
cd matplotlib
python setup.py install
```

Just use source compiled opencv libraries (don't install through pip) 

## 2. Testing

Run test on `test_opencv`