import React, { Component } from 'react';
import Moment from 'moment';
import {
  Text,
  StyleSheet,
  ScrollView,
  View,
  Dimensions,
  TouchableOpacity,
  ActivityIndicator,
  FlatList,
} from 'react-native';
import { Calendar, Agenda } from 'react-native-calendars';
/** Implement the agenda function and show the class information on each day for the trainer
* The class AgendaScreen appears as an individual screen in mobile application
* Author: Haonan Chen 
* Comment By: Haonan Chen 
*/
export default class AgendaScreen extends Component {
  /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);
    this.state = {
      // items store the course information locally for each date
      items: {},
      isLoading: true,
      dataSource: [],

    };
  }
  
  /** Retrieve the course information from the server database
    */
  componentDidMount() {
    return fetch('http://13.55.166.98/testnew.php', {
      // Standardized 'POST' method to get the information from database
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

   /** Generate the calendar of courses using the "Agenda" package 
   */
  render() {
    return (
      <Agenda
        items={this.state.items}
        // "data" stores all information from the server database
        data={this.state.dataSource}
        // fill the course information into the row in agenda
        loadItemsForMonth={this.updateCalendar.bind(this)}
        selected={'2017-05-16'}
  // generate the row of each date in agenda 
  // For the dates that have course information (classes exist in that day), generate a button on the course information
  // This button will navigate the user to the class details page
  renderItem = { this.renderItem.bind(this) }
  renderEmptyDate = { this.renderEmptyDate.bind(this) }
  rowHasChanged = { this.rowHasChanged.bind(this) }
    />
    );
}

/** The method to mark dates that have classes
 * For each date that has a class, mark the date and fill the course information into the item list 
 * @param day the date object in calendar
 */
updateCalendar(day){

  setTimeout(() => {
    // use a for loop to limit the mark dates, otherwise the calendar will mark all dates due to the original setting of Agenda package
    for (let i = -15; i < 85; i++) {
      const time = day.timestamp + i * 24 * 60 * 60 * 1000;
      const strTime = this.timeToString(time);
      if (!this.state.items[strTime]) {
        this.state.items[strTime] = [];
        this.state.dataSource.map((e) => {
          const eventTime = this.timeToString(e.start);
          const course = e.title;
          const classid = e.id;
          // if the course date is equal to the current date object, mark the date and fill in the course information 
          if (strTime === eventTime) {
            this.state.items[strTime].push({
              ID: classid ,
              Class: course ,
              height: 100
            });
          }
        });
      }
    }
    
    const newItems = {};
    Object.keys(this.state.items).forEach(key => { newItems[key] = this.state.items[key]; });
    this.setState({
      items: newItems
    });
  }, 1000);



}

// the method to navigate to "Class Details" page
onClassdetailsPress(item) {
  this.props.navigator.push({
    screen: 'ClassDetails',
    title: 'Class Details',
    passProps:{
      classid:item.ID,
    }

  });
}
// generate a button on the course information, which can navigate to "Class Details" page
renderItem(item) {
  return (

    <View style={[styles.item, { height: item.height }]}>
      <TouchableOpacity style={styles.menu} onPress={this.onClassdetailsPress.bind(this)}>
        <Text>{item.ID}</Text>
        <Text>{item.Class}</Text>
      </TouchableOpacity>
    </View>
  );
}
// Show a message for the dates that have no course 
renderEmptyDate() {
  return (
    <View style={styles.emptyDate}><Text>This is empty date!</Text></View>
  );
}

rowHasChanged(r1, r2) {
  return r1.name !== r2.name;
}
// parse the time string of course information into a specific format
timeToString(time) {
  const date = new Date(time);
  return Moment(time).format("YYYY-MM-DD");
}
}

/** The following const defines the styles of calendar and corresponding texts
*/
const styles = StyleSheet.create({
  calendar: {
    borderTopWidth: 1,
    paddingTop: 5,
    borderBottomWidth: 1,
    borderColor: '#eee',
    height: 350
  },
  text: {
    textAlign: 'center',
    borderColor: '#bbb',
    padding: 10,
    backgroundColor: '#eee'
  },
  container: {
    flex: 1,
    backgroundColor: 'white'
  },
  textForm: {
    fontWeight: 'bold',
    color: 'purple',
    position: 'absolute', 
    fontSize: 20,
    alignItems: 'center',
    justifyContent: 'flex-end',
    textAlign: 'center',

  },
  item: {
    backgroundColor: 'white',
    flex: 1,
    borderRadius: 5,
    padding: 10,
    marginRight: 10,
    marginTop: 17
  },
  emptyDate: {
    height: 15,
    flex: 1,
    paddingTop: 30
  },
});
