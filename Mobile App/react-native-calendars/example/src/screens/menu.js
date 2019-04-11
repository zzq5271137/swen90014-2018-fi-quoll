import React, { Component } from 'react';
import {
  Text,
  View,
  TouchableOpacity,
  StyleSheet,
  AppRegistry
} from 'react-native';
import { createBottomTabNavigator } from 'react-native-navigation'
import Agenda from './agenda'
import Inventory from './inventory'
/** Implement a menu screen for Inventory and Classes page
* The class MenuScreen appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen 
*/
export default class MenuScreen extends Component {
  // generate a menu for Inventory and Classes page
  // Two buttons are generated in the menu, one is for Inventory page, another is for Classes page
  render() {
    return (
      <View>
        <TouchableOpacity style={styles.menu} onPress={this.onInventoryPress.bind(this)}>
          <Text style={styles.menuText}>Inventory</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.menu} onPress={this.onAgendaPress.bind(this)}>
          <Text style={styles.menuText}>Classes</Text>
        </TouchableOpacity>
      </View>
    );
  }

  // Generate a navigator to Inventory page
  onInventoryPress() {
    this.props.navigator.push({
      screen: 'Inventory',
      title: 'Inventory'
    });
  }

 // Generate a navigator to Agenda Page 
  onAgendaPress() {
    this.props.navigator.push({
      screen: 'Agenda',
      title: 'Classes'
    });
  }
}

/** The following const defines the styles of the menu 
*/
const styles = StyleSheet.create({
  menu: {
    height: 50,
    justifyContent: 'center',
    paddingLeft: 15,
    borderBottomWidth: 1
  },
  menuText: {
    fontSize: 18
  }
});