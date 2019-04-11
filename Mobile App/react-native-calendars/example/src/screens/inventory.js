import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View,
  TouchableOpacity
} from 'react-native';

import MultipleChoice from 'rn-multiple-choice';
/** Generate a list of inventory to implment the inventory management
 * Also, this screen can add new equipment into the server
 * There are two navigation in this screen: 
 * 1. navigate to Status page to check the status of the inventory
 * 2. navigate to AddEquipment page to add the equipment into the inventory
* The class Inventory appears as an individual screen in mobile application
* Author: Haonan Chen 
* Comment by: Haonan Chen
*/
class Inventory extends Component {
  /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);
    this.state = {
      items: {},
      isLoading: true,
      // "dataSource" array stores the information of inventory from the server database 
      dataSource: [],
      // "data" array stores the information of inventory locally for generating a checklist of inventory items
      data: [],
      code: '',

    };

  }
  /** Fetch the information of inventory from the server database
   */
  componentDidMount() {
    return fetch('http://13.55.166.98/getInventory.php', {
       // Standardized 'POST' method to retrieve the information from database
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        userid:'5'
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

 /** Generate a checklist of inventory equipments
  */
  render() {
    // Check the type of inventory and store its information into "data" array
    this.state.dataSource.map((e) => {
      var type = ' ';
      if(e.item_type == '1') {
         type = 'Water Extinguisher';
      }
      else if(e.item_type == '2'){
        type = 'CO2 Extinguisher';
      }
      else{
        type = 'Foam Extinguisher';
      }
      this.state.data.push(e.item_code + ' ' + type);
    });
    // Generate a checklist of equipments and add a button at the bottom of this page
    // This button is used to add equipment to the server database 
    return (
      <View style={styles.container}>
        <MultipleChoice
          options={this.state.data}  
          // for each inventory item, when clicking, it will jump to the Status page                     
          onSelection={(option) => this.toStatus(option)}
        />
        // the button is used to navigate to AddEquipment page 
        <TouchableOpacity style={styles.menu} onPress={this.onEquipmentPress.bind(this)}>
          <Text style={styles.menuText}>Add Equipment</Text>
        </TouchableOpacity>
      </View>
    );
  }
  // navigation to AddEquipment page
  onEquipmentPress() {
    this.props.navigator.push({
      screen: 'AddEquipment',
      title: 'Add Equipment'
    });
  }
  
  // navigation to Status page and transfer the inventory id to Status page 
  toStatus(option){
    this.props.navigator.push({
      screen: 'Status',
      title:'Status',
      passProps:{
        code: option.substring(0,15),
      }
    });
  }
}
/** The following const defines the styles of text on the screen 
*/
const styles = StyleSheet.create({
  container: {
    marginTop: 60,
    margin: 20
  },
});

export default Inventory
