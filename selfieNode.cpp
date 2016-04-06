#include "ros/ros.h"
#include <k2_client/k2_client.h>
#include <k2_client/BodyArray.h>
#include <geometry_msgs/Twist.h>
#include <nav_msgs/Odometry.h>
#include <tf/transform_listener.h>
#include <signal.h>
#include <string>
#include <sstream>

using namespace std;

//os::Publisher personPos_pub;
//os::Publisher selfieScript_pub;
//geometry_msgs::Twist vel_msg;

ros::Time prev_time;
//float prev_vel_z;
//float vel_inc = 0.05;
//float vel_target = 0.3;

//bool aboveAngle = false;
//bool aboveLength = false;
//bool prevAboveAngle = false;
//bool prevAboveLength = false;

//int underLenCount = 0;


void bodies_sub_cb(const k2_client::BodyArray msg){
  alarm(1);
  for(int i = 0; i < 6; i++){
    if(msg.bodies[i].jointPositions[0].position.z < 1.4 && msg.bodies[i].jointPositions[0].position.z > 0.0){
       //Ask for selfie
      // ??.publish(msg??)
//      ROS_INFO_STREAM("Publishing message to selfie");
//      std::stringstream ss;
//      ss << "Test: " << msg.bodies[i].jointPositions[0].position.z;
      ROS_INFO("%f", msg.bodies[i].jointPositions[0].position.z);
      //selfieScript_pub.publish("1")
    }
  }
}


int main(int argc,char **argv){
  ros::init(argc,argv,"selfieNode");
  ros::NodeHandle n;

  prev_time = ros::Time::now();

  // Set up watchdog
//  signal(SIGALRM, watchdog);
//  alarm(3);

  // Set up velocity command publisher
//  personPos_pub = n.advertise<geometry_msgs::Twist>("RosAria/cmd_vel",1);

  // Set up selfieScript publisher
  //selfieScript_pub = n.advertise<std_msgs::String>("selfie", 1);

  // Subsribe to topic "bodyArray" published by k2_klient package node startBody.cpp
  ros::Subscriber bodies_sub = n.subscribe("head/kinect2/bodyArray", 1, bodies_sub_cb);

  ros::Rate loop_rate(6); //0.1

  ROS_INFO_NAMED("selfieNode", "selfieNode: Running ROS node...");
  while (ros::ok()){
    ros::spinOnce();
    loop_rate.sleep();
  }

  ROS_INFO_NAMED("selfieNode",  "selfieNode: Quitting... \n" );

  return 0;
}

