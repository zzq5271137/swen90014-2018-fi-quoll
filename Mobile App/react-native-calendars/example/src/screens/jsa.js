'use strict';
import React, { Component } from 'react';
import {
  Text,
  View,
  StyleSheet,
  ScrollView,
  FlatList,
  CheckBox,
  AppRegistry,
  TouchableOpacity,
  Linking,
  Alert,
  Dimensions,
  TextInput, 
  Button
} from 'react-native';

import MultipleChoice from 'react-native-multiple-choice'

/** Implement the checklist of JSA
* The class Jsa appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen 
*/
export default class Jsa extends Component {


  constructor(props) {
    super(props);
    this.state = {

    };
  }
  
  /** Update the JSA content to the server database
   */
  UpdateJSAContent = () => {
    // store the JSA information into a local const 
    const { JSAContent } = this.state;

    fetch('http://13.55.166.98/write_jsa.php', {
      // Use POST method to update the JSA content into the server database. 
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        content: JSAContent,
        classid: '4',
      })

    }).then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);

      }).catch((error) => {
        console.error(error);
      });
  }
  
  // generate the checklist of JSA content 
  render() {
    return (
      <ScrollView>
        <MultipleChoice
          options={[
            'Slips, trips and falls',
            'Suitable distance from flammables',
            'Placement of fuel cans and small gear',
            'PPE fit for purpose',
            'Establish a Safety Officer; top standby to assist as necessary'
          ]}
          selectedOptions={['Lorem ipsum']}
          maxSelectedOptions={5}
        // onSelection={(option)=>alert(option + ' was selected!')}
        />

        
        /**
         * Genreate other contents on this screen, below the JSA checklist 
         */
        <View style={{ flex: 1 }}>
          <Text style={{
            fontSize: 20, fontWeight: '700',
            paddingHorizontal: 10
          }}>Hazards, Risks and Controls</Text>
        </View>
        <Text style={{ fontSize: 18, fontWeight: '600', paddingHorizontal: 10 }}>Protecting the Client
       from airborne dust or pollutants and radiated heat of Flammable liquids</Text>
        <Text style={{ fontSize: 18, fontWeight: '300', paddingHorizontal: 10 }}>Risk assessment/Descriptions
Air born extinguishing agents as well as smoke form a low risk environmental hazard to people down wind of the training event.</Text>
        <Text style={{ fontSize: 18, fontWeight: '600', paddingHorizontal: 10 }}>Protecting the environment and Built Infrastructure</Text>
        <Button title="Submit" onPress={this.UpdateJSAContent} color="#2196F3" />
      </ScrollView>
    );
  }
}
