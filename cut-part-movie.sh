#!/bin/bash

./rmNeedless.sh #usuwa zastane pliki mp4 etc
link_to_yt="$1"
output_name="$2"
start_cut="$3"
end_cut="$4"
#youtube-dl --extract-audio --audio-format mp3 --output "%(uploader)s%(title)s.%(ext)s" http://www.youtube.com/watch?v=rtOvBOTyX00
youtube-dl -o "$output_name" "$link_to_yt"
# nie wiem jakie bedzi mial rozszerzenie plik stad to wyszukiwanie
download_file=$(find *.m*)
echo "$(find *.m*)"
echo "$download_file"
#ffmpeg -i original.mp4 -ss 00:01:52 -c copy -t 00:00:10 output.mp4
ffmpeg -i "$download_file" -ss "$start_cut" -c copy -to "$end_cut" "cut""$download_file" 
python loginYoutube.py
nautilus .
