
## Preparing Video

options:  160p (worst), 360p, 480p, 720p, 720p60, 1080p60
note: doesn't work for start position 00:00:00 -- need to cut video using ffmpeg. 
```
streamlink https://www.twitch.tv/videos/440478286 720p --hls-start-offset 00:11:30 --hls-duration 00:01:00 -o 440478286.mp4
```

## Testing Images Logo Detection


## Logo Detection on Video 

python logo_detection.py videos/440478286_o1220_q720.mp4

## Creating Video from set of Images

NOTE: get resolution and fps from using `ffmpeg -i <video_file>`

```
ffmpeg -r 30 -f image2 -s 640x360 -i frame%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p output.mp4
ffmpeg -r 30 -f image2 -s 1280x720 -i stage/frame%04d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p videos/440478286_o1220_q720_results.mp4

ffmpeg -ss 00:00:00 -i videos/440478286_q720_d30m.mp4 -c copy -t 00:30:00 videos/440478286_q720_cut.mp4

# create one frame from offset
# note: takes awhile for large files or on large offset (?) 
ffmpeg -i videos/440478286_o1130_q480.mp4 -f image2 -ss 00:00:15 -vframes 1 test.png

# create frame 1 sec per frame 
ffmpeg -i videos/440478286_o1220_q360.mp4 -vf fps=1 stage/frame%03d.png

# convert video to animated gif 1 sec per frame 
ffmpeg -i videos/440478286_o1220_q360.mp4 -r 1 videos/out2.gif

# create preview image select frame every 30 frames  
ffmpeg -i videos/440478286_o1220_q360.mp4 -frames 1 -q:v 1 -vf "select=not(mod(n\,30)),scale=-1:120,tile=10x3" videos/preview.jpg
 

# flags
-loop 0 -- enable loop 
-an -- no audio 

```

### Full Cycle

```
rm stage/*.png

# outputing to stage/*.png 
python logo_detection.py videos/<video_file>

# create movie with logo detection
ffmpeg -r 30 -f image2 -s 1280x720 -i stage/frame%03d.png -vcodec libx264 -crf 25  -pix_fmt yuv420p videos/<video_file>_results.mp4

```



