// Solution - As discussed by the fellow classmate in class
// modified by nehal
package U.CC;
 import java.io.IOException;

 import org.apache.hadoop.io.Writable;
 import org.apache.hadoop.io.WritableComparable;
 import org.apache.hadoop.mapred.MapReduceBase;
 import org.apache.hadoop.mapred.Mapper;
 import org.apache.hadoop.mapred.OutputCollector;
 import org.apache.hadoop.mapred.Reporter;
 import org.apache.hadoop.io.Text;


 public class BTCMapper2 extends MapReduceBase implements Mapper<WritableComparable, Writable, Text, Text> {


   public void map(WritableComparable key, Writable value,
                   OutputCollector output, Reporter reporter) throws IOException {



     // get the current page
     String data = ((Text)value).toString();
     String[] splits = data.split(": ");

     String u_new = splits[0].trim(); // hash_unique sender or receiver
     String tr_data = splits[1].trim(); // old rep usr, tr, date, amt

    
     String tr = "";
  
       if(tr_data.indexOf("to")!=-1){
       // System.out.println(tr_data);
        String[] usr_tr = tr_data.split(" ")[1].split(",");
       // System.out.println(tr_data.split(" ")[1]+" "+usr_tr[2]);
        String usr1 = u_new;
        String usr2 = usr_tr[0];
        String trn = usr_tr[1]+","+usr_tr[2]+","+usr_tr[3];
        output.collect(new Text(trn), new Text(usr1+"&S"));
    
       }
       if(tr_data.indexOf("from")!=-1){

        String[] usr_tr = tr_data.split(" ")[1].split(",");
        String usr2 = u_new;
        String usr1 = usr_tr[0];
        String trn = usr_tr[1]+","+usr_tr[2]+","+usr_tr[3];
        output.collect(new Text(trn), new Text(usr2+"&R"));

       }
	   
	  


   }
 }
