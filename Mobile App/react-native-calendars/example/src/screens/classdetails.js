import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  ScrollView,
  Image,
  FlatList,
  TouchableOpacity
} from 'react-native';
import ReqClass from './components/classdetails/ReqClass'
/** Implement the class details page, this page will show all choices associated with this class 
* The class ClassDetails appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment by: Haonan Chen
*/
export default class ClassDetails extends Component {
 /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);
    this.state = {
      classid:'',
      items: {},
      isLoading: true
    };
  }
  /** Retrieve the class id from the server database 
   */
  componentDidMount() {
    this.state.classid = this.props.classid;
    return fetch('http://13.55.166.98/read_class_info.php', {
      // Standardized 'POST' method to retrieve the information from database
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        classid: '2',
      })
    })
      .then((response) => response.json())
      .then((responseJson) => {

        this.setState({
          isLoading: false,
          dataSource: responseJson.ClassDetails,
        }, function () {
        });

      })
      .catch((error) => {
        console.error(error);
      });
  }
  
  // Genereate a list view of choices for each class
  // Such choices inclide: "Tools & Equips" , "Note" , "JSA Checklist" , "Attendance", "Mark Extinguisher" , "Leave Comment", "Feedback", "Qualifications", "Customer Sign Off" 
  // Each choice has a "Edit" button which can navigate to a new page to edit the content of this page
  render() {
    return (
      <ScrollView>
        <View style={{ flex: 1, paddingTop: 20 }}>
          <FlatList
            data={this.state.dataSource}
            renderItem={({ item }) =>
              <Text> {item.contact_name}
                Trainer: {item.trainer_first_name}, {item.trainer_last_name},{item.title},{item.class_location},{item.start},{item.end}</Text>}

            keyExtractor={({ id }, index) => id}
          /></View>

        <View style={{ flex: 1 }}>
          <Text style={{
            fontSize: 20, fontWeight: '700',
            paddingHorizontal: 10
          }}>Details for this class</Text>
        </View>

        <ReqClass itemm="Tools & Equips" imageUri={require('../assets/firefighter.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onInventoryPress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
        <ReqClass itemm="Note" imageUri={require('../assets/todo.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onNotePress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>

        <View>
          <Text style={{
            fontSize: 20, fontWeight: '100', padding: 10,
            paddingHorizontal: 10
          }}>Need to go over basic fire drills. There has been some confusion as to steps 4-6.</Text>
        </View>

        <ReqClass itemm="JSA Checklist" imageUri={require('../assets/todo.png')} />

        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onJsaPress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>

        <ReqClass itemm="Attendance" imageUri={require('../assets/todo.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onAttendeePress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
        <ReqClass itemm="Mark Extinguisher" imageUri={require('../assets/extinguisher.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onInventoryPress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
        <ReqClass itemm="Leave Comment" imageUri={require('../assets/todo.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onCommentPress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
        <ReqClass itemm="Feedback" imageUri={require('../assets/todo.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onFeedbackPress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
        <ReqClass itemm="Qualifications" imageUri={require('../assets/todo.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onQualificationPress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
        <ReqClass itemm="Customer Sign Off" imageUri={require('../assets/todo.png')} />
        <View style={{ flex: 1, flexDirection: 'row', justifyContent: 'flex-end' }}>

          <TouchableOpacity style={styles.menu} onPress={this.onSignaturePress.bind(this)}>
            <Text>EDIT</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    );
  }

   // Construct the navigations to different screens
  onCommentPress() {
    this.props.navigator.push({
      screen: 'Comment',
      title: 'Leave Comment'
    });
  }

  onInventoryPress() {
    this.props.navigator.push({
      screen: 'Inventory',
      title: 'Inventory'
    });
  }

  onAgendaPress() {
    this.props.navigator.push({
      screen: 'Agenda',
      title: 'Classes'
    });
  }

  onClassdetailsPress() {
    this.props.navigator.push({
      screen: 'ClassDetails',
      title: 'Class Details'
    });
  }

  onJsaPress() {
    this.props.navigator.push({
      screen: 'Jsa',
      title: 'JSA'
    });
  }

  onSignaturePress() {
    this.props.navigator.push({
      screen: 'Signature',
      title: 'Customer Sign Off'
    });
  }

  onAttendeePress() {
    this.props.navigator.push({
      screen: 'Attendee',
      title: 'Attendee'
    });
  }
  onQualificationPress() {
    this.props.navigator.push({
      screen: 'Qualification',
      title: 'Qualification'
    });
  }

  onNotePress() {
    this.props.navigator.push({
      screen: 'Note',
      title: 'Note'
    });
  }

  onFeedbackPress() {
    this.props.navigator.push({
      screen: 'Feedback',
      title: 'Feedback'
    });
  }
}


const styles = StyleSheet.create({
  item: {
    backgroundColor: 'white',
    flex: 1,
    borderRadius: 5,
    padding: 10,
    marginRight: 10,
    marginTop: 17
  },
});
