import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  Image,
  TouchableOpacity,
} from 'react-native';
//import MenuScreen from './menu'
/** Defines the style of list view in ClassDetails page. Set the style for each choice in the list.
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/
class ReqClass extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <View>
        <View style={{ flexDirection: 'column', padding: 20, backgroundColor: 'white' }}>
          <View style={{ flexDirection: 'row' }}>
            <Image source={this.props.imageUri} style={{ width: 40, height: 40 }} />
            <Text style={{ fontSize: 20, fontWeight: '300', paddingHorizontal: 10 }}>{this.props.itemm}</Text>
          </View>
        </View>
        <View style={{ height: this.startHeaderHeight, backgroundColor: 'white', borderBottomWidth: 1, borderBottomColor: '#dddddd' }}></View>
      </View>
    );
  }
}
export default ReqClass;

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