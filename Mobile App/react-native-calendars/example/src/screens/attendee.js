import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View
} from 'react-native';

import MultipleChoice from 'rn-multiple-choice';
/** Implement the check of students' attendance 
* The class Attendee appears as an individual screen in mobile application
* Author: Haonan Chen 
* Comment By: Haonan Chen 
*/
class Attendee extends Component {
  /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);
    this.state = {
      items: {},
      isLoading: true,
      // dataSource array stores the information of students from server database
      dataSource: [],
      // data array stores the information of students locally 
      data: [],

    };

  }
  
  /** Fetch the information of students of the course from the server database 
   */
  componentDidMount() {
    return fetch('http://13.55.166.98/getAttendee.php', {
      // Standardized 'POST' method to retrieve the information of students
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        userid: '5',
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
 
  /** Update the information of students selected on the server database
   * If a student attends the class, the trainer will click to check the attendance
   * Then, when clicking, the server database will update the field "attended" in database
   * When "attended" is 0, it means the students are absent. If "attended" is 1, it means the students attend.
   * @param option the object that stores the information for each student
   */
  onSelectionsChange(option) {

    fetch('http://13.55.166.98/updateAttendee.php', {
      // Standardized 'POST' method to upload the information of students
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        id: option.substring(0, 1),
        attended: '1',
      })

    }).then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);

      }).catch((error) => {
        console.error(error);
      });
  }


  render() {
    // Transfer the data of students into the local "data" array
    this.state.dataSource.map((e) => {
      // store id, first name and last name of students in "data" array 
      this.state.data.push(e.id + ' ' + e.first_name + ' ' + e.last_name);
    });
    // generate a checklist for students enrolling in this classs 
    return (
      <View style={styles.container}>
        
        <MultipleChoice
          options={this.state.data}
          onSelection={(option) => this.onSelectionsChange(option)}
        />
      </View>
    );
  }
}

/** The following const defines the styles of the screen 
*/
const styles = StyleSheet.create({
  container: {
    marginTop: 20,
    margin: 20
  },
});

export default Attendee
