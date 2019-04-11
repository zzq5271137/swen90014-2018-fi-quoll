import React, { Component } from 'react';
import {
    StyleSheet,
    View,
    TextInput,
    Button
} from 'react-native';
/** Implement the addition of equipmemnt to the database
* The class AddEquipment appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/
export default class AddEquipment extends Component {
    /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
    constructor(props) {
        super(props);
        this.state = {
            EquipmentID:' ',
            EquipmentType:' ',
        };
    }

    /** Insert the data of equipment information to the server database
    */
    InsertDataToServer = () => {
        // define two variables to store the equipment id and euipment type to be uploaded
        var uploadEquipmentID  = this.state.EquipmentID;
        var uploadEquipmentType  = this.state.EquipmentType;
        // Standardized 'POST' method to upload the information to database
        fetch('http://13.55.166.98/write_equipment.php', {
            method: 'POST',
            header: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            // Use JSON stringify method to upload the information to backend database, 
            // id & type are the "field name" in the corresponding table in database
            body: JSON.stringify({

                id: uploadEquipmentID,
                type: uploadEquipmentType,
            })

        }).then((response) => response.json())
            .then((responseJson) => {
                alert(responseJson);

            }).catch((error) => {
                console.error(error);
            });

    }

    /** Generate the screen to type in the information of equipment 
    * In this screen, there are two placeholders to let the user type in the id and type of the equipments
    * Then, by clicking the button "Add Equipment", the information of equipment will be uploaded.
    */
    render() {
        return (

            <View style={styles.MainContainer} >

                <TextInput

                    // Adding hint in Text Input using Place holder.
                    placeholder="Enter Equipment ID"

                    onChangeText={
                        (text) => this.setState({
                            EquipmentID : text 
                        })
                    }

                    // Making the Under line Transparent.
                    underlineColorAndroid='transparent'

                    style={styles.TextInputStyleClass
                    } />

                <TextInput

                    // Adding hint in Text Input using Place holder.
                    placeholder="Enter EquipmentType"

                    onChangeText={
                        (text) => this.setState({
                            EquipmentType : text 
                        })
                    }

                    // Making the Under line Transparent.
                    underlineColorAndroid='transparent'

                    style={
                        styles.TextInputStyleClass
                    } />
               
                
                <Button title="Add Equipment"
                    onPress={
                        this.InsertDataToServer
                    }
                    color="#2196F3" />


            </View>

        );
    }

}


/** The following const defines the styles of text on the screen 
*/
const styles = StyleSheet.create({

    MainContainer: {
  
      justifyContent: 'center',
      flex: 1,
      margin: 10
    },
  
    TextInputStyleClass: {
  
      textAlign: 'center',
      marginBottom: 7,
      height: 40,
      borderWidth: 1,
      // Set border Hex Color Code Here.
      borderColor: '#FF5722',

    }
  
  });