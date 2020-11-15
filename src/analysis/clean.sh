
# this script convert test.bag in 
# use topic of /camera/image_raw
# https://wiki.ros.org/rosbag/Tutorials/Exporting%20image%20and%20video%20data
roscd image_view
rosmake image_view
sudo apt-get install mjpegtools

output=export.launch

echo "<launch>" | tee -a $output
echo "<node pkg="rosbag" type="play" name="rosbag" required="true" args="$(find image_view)/test.bag"/>" | tee -a $output
echo "<node name="extract" pkg="image_view" type="extract_images" respawn="false" required="true" output="screen" cwd="ROS_HOME">" | tee -a $output
echo "<remap from="image" to="/camera/image_raw"/>" | tee -a $output
echo "</node>" | tee -a $output
echo "</launch>" | tee -a $output

roslaunch export.launch

# the output dir of frame
cd ~
mkdir jpeg_frame
mv ~/.ros/frame*.jpg  jpeg_frame






