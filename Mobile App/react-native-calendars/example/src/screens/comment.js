import React, { Component } from 'react';
import { AppRegistry, StyleSheet, View, Text, TextInput, Button } from 'react-native';
/** Implement the comment field, the user can add comment on this page and update it to database
* The class Comment appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/
export default class Comment extends Component {
   /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props)
    this.state = {
      text: ' ',
      CommentContent: '',
    }
  }
 
  /** Update the comment to server database as text 
   */
  UpdateComment = () => {

    const { CommentContent } = this.state;

    fetch('http://13.55.166.98/write_jsa.php', {
      // Standardized 'POST' method to upload the information to database
      method: 'POST',
      header: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        content: CommentContent,
        classid: '2',
      })

    }).then((response) => response.json())
      .then((responseJson) => {
        alert(responseJson);

      }).catch((error) => {
        console.error(error);
      });
  }
  // Generate the screen to add commnet and the button to submit the comment  
  render() {
    return (
      <View>
        <View style={styles.container}>
          <Text style={{
            fontSize: 20, fontWeight: '700',
            paddingHorizontal: 10
          }}>Comment</Text>
        </View>
        <TextInput multiline style={{ maxHeight: 400, borderColor: 'gray', borderWidth: 1 }}
          onChangeText={(CommentContent) => this.setState({ CommentContent })}
          value={this.state.text} />
        <Button title="Submit" onPress={this.UpdateComment} color="#2196F3" />
      </View>
    );
  }
}

/** The following const defines the styles of comment on the screen 
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
