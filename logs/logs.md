# Logs

*im just gonna leave little progress notes here, along with my plans and stuff*

## 3/17/2025

wow, new repository, what's this for? yep, another hack club YSWS. im gonna try to speedrun this one in two days! (i did another one in 2 hours and another one in 15 minutes before...)

basically, make something in the terminal! and since the YSWS is called `terminal-craft`, that's exactly what im gonna try to do. terminal craft. like 3d minecraft in the terminal (2d is silly)

![waw](</logs/images/03172025 - 1.png>)

colored display in terminal!

and now here's a bigger display!

![waw](</logs/images/03172025 - 2.png>)

having a couple strange issues with lag or what not, so gonna try to fix that! it appears that clearing the screen is taking a bit, so thats interesting... anyways, good night! (wait hows it 2am already)

# 3/18/2025

was too tired lol, anyways, wrote lots of bits about the player camera, and theoretically the renderer, and world and stuff

# 3/19/2025

ok, last day to work on it, ready to work on it for the next three hours...

ok, fixed the weird crashing by changing the camera projection matrix to 4x4 instead of 3x3, now its just a black screen...

ok, been working on some stuff, and rendering seems to be starting to work, inputs also are listening (using the `keyboard` module), player is moving and added some debug log thing! still need to write something for rendering lines (so we get, you know, cubes and stuff)

ok, rendering stuff, we got a very vibrant green cube! it also seems that we dont really have any "is it behind me" detection, as i think we are seeing behind ourselves?