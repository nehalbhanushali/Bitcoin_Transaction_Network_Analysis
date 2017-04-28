//
 // Author - Jack Hebert (jhebert@cs.washington.edu)
 // Copyright 2007
 // Distributed under GPLv3
 //
// Modified - Dino Konstantopoulos
// Distributed under the "If it works, remolded by Dino Konstantopoulos,
// otherwise no idea who did! And by the way, you're free to do whatever
// you want to with it" dinolicense
//
package U.CC;

 import org.apache.hadoop.fs.Path;
 import org.apache.hadoop.io.IntWritable;
 import org.apache.hadoop.io.Text;
 import org.apache.hadoop.mapred.JobClient;
 import org.apache.hadoop.mapred.JobConf;
 import org.apache.hadoop.mapred.Mapper;
 import org.apache.hadoop.mapred.Reducer;

import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;


 public class BTCDriver2 {

 public static void main(String[] args) {
 JobClient client = new JobClient();
 JobConf conf = new JobConf(BTCDriver2.class);
 conf.setJobName("BTC  Driver");

 conf.setNumReduceTasks(5); //?

 //~dk
 //conf.setInputFormat(org.apache.hadoop.mapred.SequenceFileInputFormat.class);
 //conf.setOutputFormat(org.apache.hadoop.mapred.SequenceFileOutputFormat.class);

 conf.setOutputKeyClass(Text.class);
 conf.setOutputValueClass(Text.class);

 if (args.length < 2) {
 System.out.println("Usage: BTC <input path> <output path>");
 System.exit(0);
 }

 //~dk
 //conf.setInputPath(new Path(args[0]));
 //conf.setOutputPath(new Path(args[1]));
 FileInputFormat.setInputPaths(conf, new Path(args[0]));
 FileOutputFormat.setOutputPath(conf, new Path(args[1]));

 //conf.setInputPath(new Path("graph2"));
 //conf.setOutputPath(new Path("graph3"));

 conf.setMapperClass(BTCMapper2.class);
 conf.setReducerClass(BTCReducer2.class);
 // conf.setCombinerClass(BTCDriver2.class); //??

 client.setConf(conf);
 try {
 JobClient.runJob(conf);
 } catch (Exception e) {
 e.printStackTrace();
 }
 }
 }
