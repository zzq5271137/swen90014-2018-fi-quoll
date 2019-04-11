import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  ScrollView,
  Image,
  FlatList,
  ListView
} from 'react-native';
import ReqClass from './components/classdetails/ReqClass'
import MultipleChoice from 'rn-multiple-choice';
/** Implement the read of qualification from the database
* The class Qualification appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/

export default class Qualification extends Component {
/** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);
    this.state = {
      items: {},
      isLoading: true,
      dataSource: [],
      data: [],
    };
  }
/** Retrieve the qualification content from the server database 
   */
  componentDidMount() {
    return fetch('http://13.55.166.98/read_qualification.php', {
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        trainerid: '4',
      })
    })
      .then((response) => response.json())
      .then((responseJson) => {

        this.setState({
          isLoading: false,
          dataSource: responseJson.Qualification,
        }, function () {
        });

      })
      .catch((error) => {
        console.error(error);
      });
  }
// Construct a scroll view and flat list for the qualification content 
  render() {

    return (
      <ScrollView>

        <View style={styles.container}>
          <Text style={{
            fontSize: 20, fontWeight: '700',
            paddingHorizontal: 10
          }}>Qualification</Text>
        </View>

        <View style={{ flex: 1, paddingTop: 10 }}>
          <FlatList
            data={this.state.dataSource}
            renderItem={({ item }) => <Text style={{
              fontSize: 20, fontWeight: '300',
              paddingHorizontal: 10
            }}>{item.qualification_name}</Text>}
            keyExtractor={({ id }, index) => id}
          />
        </View>
      </ScrollView>
    );
  }
}
/** The following const defines the styles of qualification content on the screen 
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
