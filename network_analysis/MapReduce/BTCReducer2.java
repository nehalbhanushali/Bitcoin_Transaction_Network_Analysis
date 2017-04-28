
package U.CC;

 import java.io.IOException;
 import java.util.Iterator;

 import org.apache.hadoop.io.WritableComparable;
 import org.apache.hadoop.mapred.MapReduceBase;
 import org.apache.hadoop.mapred.OutputCollector;
 import org.apache.hadoop.mapred.Reducer;
 import org.apache.hadoop.mapred.Reporter;
 import org.apache.hadoop.io.Text;

 public class BTCReducer2 extends MapReduceBase implements Reducer<WritableComparable, Text, Text, Text> {

   public void reduce(WritableComparable key, Iterator values,
                      OutputCollector output, Reporter reporter) throws IOException {

   
     String trn = key.toString();

     String trn_arr[]= trn.split(",");
     String trn_idx = trn_arr[0];
     String time_stmp = trn_arr[1];
     String cost = trn_arr[2];
     String usr1= "";
     String usr2= "";
   
     while (values.hasNext())
     {
	   String usr_info = ((Text)values.next()).toString();
	   try{
       if(usr_info.indexOf("&S")!=-1){
		   
       usr1= usr_info.split("&S")[0];
       }
       if(usr_info.indexOf("&R")!=-1){
       usr2= usr_info.split("&R")[0];
       }
	 
	   }
	   catch(Exception e){
	
	   }
     }
	 
    if(!usr1.equals("") && !usr2.equals(""))
	{	
	usr1= usr1.split("#")[1];
	usr2= usr2.split("#")[1];
    output.collect(new Text(trn_idx+","+usr1+","+usr2+","+time_stmp+","+cost), new Text("")); 
	}
	else{
	System.out.println(":::::::::::::::::: usr1 "+usr1+" usr2 "+usr2+"");	
   }
   
   
  } 
   
 }
