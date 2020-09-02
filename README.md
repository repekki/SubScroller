# Youtube Subscriber count Scroller
Youtube subscription counter that scrolls custom text and subcount

## What you need
- An Arduino board of your choice. I used Arduino Uno.
- Raspberry Pi
- 8x8 max7219

## What you need to do on Arduino

- You need the MaxMatrix library.
- Edit the example code to fit your needs and upload it to Arduino.
- Look at the schematic and connect the wires as instructed.
  - ![Wiring](/img/subcounter_scema_bb.png)
- Plug the USB into your Raspberry Pi.

## What you need to do on Raspberry Pi

- Install a web server of your choice. I used Apache.
- In the folder */var/www/html/* create the file **index.php** and remove **index.html**
  - Now the landing page of the webserver is **index.php**
- **index.php** saves the subscriber count and any text you submit through the form to two different files.
- **filereader_serialwriter.py** changes those files into strings so Arduino can read them, opens the serial port and sends the data over to Arduino.
- **watchMod.py** watches the text files for changes and when they are overwritten, it automatically runs *filereader_serialwriter.py*
- When you want to use the program, you need to run **watchMod.py**

