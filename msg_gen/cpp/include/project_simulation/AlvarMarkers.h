/* Auto-generated by genmsg_cpp for file /home/shray/groovy_workspace/sandbox/project_simulation/msg/AlvarMarkers.msg */
#ifndef PROJECT_SIMULATION_MESSAGE_ALVARMARKERS_H
#define PROJECT_SIMULATION_MESSAGE_ALVARMARKERS_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"
#include "project_simulation/AlvarMarker.h"

namespace project_simulation
{
template <class ContainerAllocator>
struct AlvarMarkers_ {
  typedef AlvarMarkers_<ContainerAllocator> Type;

  AlvarMarkers_()
  : header()
  , markers()
  {
  }

  AlvarMarkers_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , markers(_alloc)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef std::vector< ::project_simulation::AlvarMarker_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::project_simulation::AlvarMarker_<ContainerAllocator> >::other >  _markers_type;
  std::vector< ::project_simulation::AlvarMarker_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::project_simulation::AlvarMarker_<ContainerAllocator> >::other >  markers;


  typedef boost::shared_ptr< ::project_simulation::AlvarMarkers_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::project_simulation::AlvarMarkers_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct AlvarMarkers
typedef  ::project_simulation::AlvarMarkers_<std::allocator<void> > AlvarMarkers;

typedef boost::shared_ptr< ::project_simulation::AlvarMarkers> AlvarMarkersPtr;
typedef boost::shared_ptr< ::project_simulation::AlvarMarkers const> AlvarMarkersConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::project_simulation::AlvarMarkers_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::project_simulation::AlvarMarkers_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace project_simulation

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::project_simulation::AlvarMarkers_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::project_simulation::AlvarMarkers_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::project_simulation::AlvarMarkers_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bf5718fe62b84cd15d9fe396f0b1de3a";
  }

  static const char* value(const  ::project_simulation::AlvarMarkers_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xbf5718fe62b84cd1ULL;
  static const uint64_t static_value2 = 0x5d9fe396f0b1de3aULL;
};

template<class ContainerAllocator>
struct DataType< ::project_simulation::AlvarMarkers_<ContainerAllocator> > {
  static const char* value() 
  {
    return "project_simulation/AlvarMarkers";
  }

  static const char* value(const  ::project_simulation::AlvarMarkers_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::project_simulation::AlvarMarkers_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
AlvarMarker[] markers\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: project_simulation/AlvarMarker\n\
Header header\n\
uint32 id\n\
geometry_msgs/PoseStamped pose\n\
================================================================================\n\
MSG: geometry_msgs/PoseStamped\n\
# A Pose with reference coordinate frame and timestamp\n\
Header header\n\
Pose pose\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Pose\n\
# A representation of pose in free space, composed of postion and orientation. \n\
Point position\n\
Quaternion orientation\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Quaternion\n\
# This represents an orientation in free space in quaternion form.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
float64 w\n\
\n\
";
  }

  static const char* value(const  ::project_simulation::AlvarMarkers_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::project_simulation::AlvarMarkers_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::project_simulation::AlvarMarkers_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::project_simulation::AlvarMarkers_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.markers);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct AlvarMarkers_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::project_simulation::AlvarMarkers_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::project_simulation::AlvarMarkers_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "markers[]" << std::endl;
    for (size_t i = 0; i < v.markers.size(); ++i)
    {
      s << indent << "  markers[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::project_simulation::AlvarMarker_<ContainerAllocator> >::stream(s, indent + "    ", v.markers[i]);
    }
  }
};


} // namespace message_operations
} // namespace ros

#endif // PROJECT_SIMULATION_MESSAGE_ALVARMARKERS_H

