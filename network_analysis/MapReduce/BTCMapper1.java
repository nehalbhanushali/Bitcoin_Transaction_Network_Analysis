
// Solution - As discussed by the fellow classmate in class
// modified by nehal

package U.CC;

import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;

import java.util.*;
import java.lang.StringBuilder;

 /*
  * @nehal
  *
  *
  */
 public class BTCMapper1 extends MapReduceBase implements Mapper<LongWritable, Text, Text, Text> {

   public void map(LongWritable key, Text value,
                   OutputCollector output, Reporter reporter) throws IOException
{
     // Prepare the input data.
    String BTC = value.toString();
    //System.out.println("< "+key.toString()+" > "+"< "+BTC+" >");

    // separating input file key and edge, selecting user key file here !!
    String BTC_usrlist_or_not[] = BTC.split(",");
    if(BTC_usrlist_or_not.length ==2){
      String unique_val = BTC_usrlist_or_not[0];
      String user_list = BTC_usrlist_or_not[1];
      output.collect(new Text(user_list+" : "), new Text("#"+unique_val));
     // System.out.println(user_list+" : "+"#"+unique_val);
    }
    else if(BTC.indexOf("\"")!=-1)
    {
     String BTC_hash_userList[] = BTC.split(",\"");
     if(BTC_hash_userList.length == 2){

    String unique_val = BTC_hash_userList[0];
    String user_list_string[] = BTC_hash_userList[1].split("\""); // remove trailing " as well

    String user_list[] = user_list_string[0].split(",");

    for (int i = 0 ; i< user_list.length;i++){
        output.collect(new Text(user_list[i]+" : "),new Text("#"+unique_val));
       // System.out.println(user_list[i]+" : "+"#"+unique_val);
    }

}
}
else if(BTC_usrlist_or_not.length ==5)
{

   String tr = BTC_usrlist_or_not[0];
   String u1 = BTC_usrlist_or_not[1];
   String u2 = BTC_usrlist_or_not[2];
   String time = BTC_usrlist_or_not[3];
   String cost = BTC_usrlist_or_not[4];

   String tr_string = tr+","+time+","+cost;

   output.collect(new Text(u1+" : "), new Text("@to "+u2+","+tr_string));
   output.collect(new Text(u2+" : "), new Text("@from "+u1+","+tr_string));
  // System.out.println(u1+" : "+"@to "+u2+","+tr_string);
  // System.out.println(u2+" : "+"@from "+u1+","+tr_string);


}

   }

 }
