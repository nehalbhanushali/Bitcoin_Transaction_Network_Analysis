// Solution - As discussed by the fellow classmate in class
// modified by nehal

package U.CC;

 import java.io.IOException;
 import java.util.Iterator;

 import org.apache.hadoop.io.IntWritable;
 import org.apache.hadoop.io.Text;
 import org.apache.hadoop.io.WritableComparable;
 import org.apache.hadoop.mapred.MapReduceBase;
 import org.apache.hadoop.mapred.OutputCollector;
 import org.apache.hadoop.mapred.Reducer;
 import org.apache.hadoop.mapred.Reporter;
 import java.lang.StringBuilder;
 import java.util.*;

 public class BTCReducer1 extends MapReduceBase implements Reducer<Text, Text, Text, Text>
{

   public void reduce(Text key, Iterator<Text> values,
                      OutputCollector<Text, Text> output, Reporter reporter) throws IOException {



     String user = key.toString();
     System.out.print(user);
     String trans_list = "";
     String hash_key = "";
   
     while (values.hasNext())
     {
        
        String hashOrTrList = ((Text)values.next()).toString();
      //  System.out.print(" "+hashOrTrList);
        if(hashOrTrList.indexOf("#")!=-1){
          // this is a user_hash
           hash_key = hashOrTrList; // new from or to
       
        }
        else if(hashOrTrList.indexOf("@")!=-1){
       
        trans_list += hashOrTrList+"::";
        
        //output.collect(new Text(hash_key+" : "), new Text(hashOrTrList));

        }
    


     }
// System.out.println();
 String array_tr[]= trans_list.split("::");
 for (int i = 0;i<array_tr.length;i++){
 output.collect(new Text(hash_key+" : "), new Text(array_tr[i]));  
 }
 // output.collect(new Text(hash_key+" : "), new Text(trans_list));
  }
 }
