import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  ScrollView,
  Image,
  FlatList,
} from 'react-native';
import ReqClass from './components/classdetails/ReqClass'
/** Implement read of note, retrieve the note from the server database
 * The class Note appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/

export default class Note extends Component {
/** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);
    this.state = {
      items: {},
      isLoading: true
    };
  }
/** Retrieve the note content from the server database 
   */
  componentDidMount() {
    return fetch('http://13.55.166.98/read_note.php', {
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
          dataSource: responseJson.Note,
        }, function () {
        });

      })
      .catch((error) => {
        console.error(error);
      });
  }
// Construct a scroll view for the note content 
  render() {
    return (
      <ScrollView>

      <View style={styles.container}>
        <Text style={{
          fontSize: 20, fontWeight: '700',
          paddingHorizontal: 10
        }}>Note</Text>
      </View>

      <View style={{ flex: 1, paddingTop: 10 }}>
        <FlatList
          data={this.state.dataSource}
          renderItem={({ item }) => <Text style={{
            fontSize: 20, fontWeight: '300',
            paddingHorizontal: 10
          }}>{item.note}</Text>}
          keyExtractor={({ event_ptr_id }, index) => event_ptr_id}
        />
      </View>
    </ScrollView>
    );
  }
}
/** The following const defines the styles of feedback content on the screen 
*/
const styles = StyleSheet.create({
  item: {
    backgroundColor: 'white',
    flex: 1,
    borderRadius: 5,
    padding: 10,
    marginRight: 10,
    marginTop: 17
  },
  container: {
    marginTop: 20,
    margin: 20
  },
});
