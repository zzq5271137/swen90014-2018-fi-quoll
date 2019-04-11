import React, { Component } from 'react';
import {
  StyleSheet,
  Text,
  View
} from 'react-native';

import MultipleChoice from 'rn-multiple-choice';
/** Implement the status update of the inventory equipment
* The class Status appears as an individual screen in mobile application
* Author: Haonan Chen 
* Comment By: Haonan Chen
*/
class Status extends Component {
  constructor(props) {
    super(props);
    this.state = {
      code:'',

    };

  }
 /** Update the status of equipments to the server database
  * @param option represent an option object
  */
  updateStatus(option){
      this.state.code = this.props.code;
      var k ='';
      // check the type of status
      if(option == 'New'){
        k = '1';
      }
      else if(option == 'Used'){
        k = '2';
      }
      else {
        k = '3';
      }
      // update the status to the server database 
      fetch('http://13.55.166.98/updateStatus.php', {
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        item_code: this.state.code,
        status: k,
      })

    }).then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);

      }).catch((error) => {
        console.error(error);
      });

  }
 

  /** Generate a list of status options
   */
  render() {
    return (
      <View style={styles.container}>
        <MultipleChoice
          options={['New','Used','Exhausted']}  
          // Since each equipment can only have 1 status at a time, we limit the maximum status an equipment can have to 1
          maxSelectedOptions={1}                     
          onSelection={(option) => this.updateStatus(option)}
        />
      </View>
    );
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

export default Status
