import processing.serial.*;
Serial myPort; //creates a software serial port on which you will listen to Arduino
Table table; //table where we will read in and store values. You can name it something more creative!
 
int numReadings = 5000; //keeps track of how many readings you'd like to take before writing the file. 
int count = 0; //counts each reading to compare to numReadings. 
int ground = 0;
int time0;
int time1 = 0;
String ms;
 
String val;
String pad;
String fileName;
void setup()
{
  table = new Table();
  String portName = "COM11"; 
  //CAUTION: your Arduino port number is probably different! Mine happened to be 1. Use a "handshake" sketch to figure out and test which port number your Arduino is talking on. A "handshake" establishes that Arduino and Processing are listening/talking on the same port.
  //Here's a link to a basic handshake tutorial: https://processing.org/tutorials/overview/
  
  myPort = new Serial(this, portName, 2000000); //set up your port to listen to the serial port
   
  //table.addColumn("id"); //This column stores a unique identifier for each record. We will just count up from 0 - so your first reading will be ID 0, your second will be ID 1, etc. 
  
  //the following adds columns for time. You can also add milliseconds. See the Time/Date functions for Processing: https://www.processing.org/reference/ 
  table.addColumn("Date");
  
  //the following are dummy columns for each data value. Add as many columns as you have data values. Customize the names as needed. Make sure they are in the same order as the order that Arduino is sending them!
  table.addColumn("sensor0X");
  table.addColumn("sensor0Y");
  table.addColumn("sensor0Z");
  table.addColumn("sensor1X");
  table.addColumn("sensor1Y");
  table.addColumn("sensor1Z");
  table.addColumn("sensor2X");
  table.addColumn("sensor2Y");
  table.addColumn("sensor2Z");
  table.addColumn("sensor3X");
  table.addColumn("sensor3Y");
  table.addColumn("sensor3Z");
  table.addColumn("sensor4X");
  table.addColumn("sensor4Y");
  table.addColumn("sensor4Z");
  table.addColumn("sensor5X");
  table.addColumn("sensor5Y");
  table.addColumn("sensor5Z");
  table.addColumn("sensor6X");
  table.addColumn("sensor6Y");
  table.addColumn("sensor6Z");
  table.addColumn("sensor7X");
  table.addColumn("sensor7Y");
  table.addColumn("sensor7Z");
 
}
 
void serialEvent(Serial myPort){
  val = myPort.readStringUntil('\n'); //The newline separator separates each Arduino loop. We will parse the data by each newline separator. 
  if (val!= null) { //We have a reading! Record it.
    if (count>7){
      time1 = second();
      if(time0!=time1){
        ground = millis();
      }
      time0 = time1;
      val = trim(val); //gets rid of any whitespace or Unicode nonbreakable space
      println(val); //Optional, useful for debugging. If you see this, you know data is being sent. Delete if  you like. 
      float sensorVals[] = float(split(val, ',')); //parses the packet from Arduino and places the valeus into the sensorVals array. I am assuming floats. Change the data type to match the datatype coming from Arduino. 
      
      TableRow newRow = table.addRow(); //add a row for this new reading
      //newRow.setInt("id", table.lastRowIndex());//record a unique identifier (the row's index)
      
      //record time stamp
      ms = str(millis()-ground);
      
      if(ms.length() == 1){
        pad = "00";
      }
      else if(ms.length() == 2){
        pad="0";
      }
      else{pad="";}
        
      String date = str(year()) + "-" + str(month()) + "-" + str(day())+" "+ str(hour())+ ":"+ str(minute())+ ":"+ str(second())+"."+pad+ms;
      newRow.setString("Date", date);
      
      //record sensor information. Customize the names so they match your sensor column names. 
      newRow.setFloat("sensor0X", sensorVals[0]);
      newRow.setFloat("sensor0Y", sensorVals[1]);
      newRow.setFloat("sensor0Z", sensorVals[2]);
      newRow.setFloat("sensor1X", sensorVals[3]);
      newRow.setFloat("sensor1Y", sensorVals[4]);
      newRow.setFloat("sensor1Z", sensorVals[5]);
      newRow.setFloat("sensor2X", sensorVals[6]);
      newRow.setFloat("sensor2Y", sensorVals[7]);
      newRow.setFloat("sensor2Z", sensorVals[8]);
      newRow.setFloat("sensor3X", sensorVals[9]);
      newRow.setFloat("sensor3Y", sensorVals[10]);
      newRow.setFloat("sensor3Z", sensorVals[11]);
      newRow.setFloat("sensor4X", sensorVals[12]);
      newRow.setFloat("sensor4Y", sensorVals[13]);
      newRow.setFloat("sensor4Z", sensorVals[14]);
      newRow.setFloat("sensor5X", sensorVals[15]);
      newRow.setFloat("sensor5Y", sensorVals[16]);
      newRow.setFloat("sensor5Z", sensorVals[17]);
      newRow.setFloat("sensor6X", sensorVals[18]);
      newRow.setFloat("sensor6Y", sensorVals[19]);
      newRow.setFloat("sensor6Z", sensorVals[20]);
      newRow.setFloat("sensor7X", sensorVals[21]);
      newRow.setFloat("sensor7Y", sensorVals[22]);
      newRow.setFloat("sensor7Z", sensorVals[23]);
      
    }    
    count++; 
   }
}
 
void draw()
{ 
   //visualize your sensor data in real time here! In the future we hope to add some cool and useful graphic displays that can be tuned to different ranges of values. 
}

void keyPressed() {
  fileName = str(year()) + "-" + str(month()) + "-" + str(day())+ ".csv"; //this filename is of the form year+month+day+readingCounter
  saveTable(table, fileName); //Woo! save it to your computer. It is ready for all your spreadsheet dreams. 
}
