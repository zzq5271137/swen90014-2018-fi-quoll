import React, { Component } from 'react';
import {
  View, StyleSheet, Text, Image, TouchableOpacity
} from 'react-native';

import SignatureView from './SignatureView';

const flexCenter = {
  flex: 1,
  justifyContent: 'center',
  alignItems: 'center',
};

/** Implement the capture of signature 
* The class Signature appears as an individual screen in mobile application
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/
class Signature extends Component {
  /** The constructor of propos of this screen component 
    * @param props the props that handles this screen 
    */
  constructor(props) {
    super(props);

    this.state = {
      data: null
    };
  }
  /** Generate the signature screen 
   * Show a message at the background of the signature screen 
   */
  render() {
    const {data} = this.state;
    return (
      <View style={flexCenter}>
        <TouchableOpacity onPress={this._showSignatureView.bind(this)}>
          <View style={[flexCenter, {padding: 10}]}>
            <Text style={{fontSize: 18, fontWeight: 'bold'}}>
              {data ? 'This is a your signature.' : 'Click here.'}
            </Text>
            <View style={{paddingBottom: 10}} />
            {data &&
              <View style={{backgroundColor: 'white'}}>
                <Image
                  resizeMode={'contain'}
                  style={{width: 300, height: 300}}
                  source={{uri: data}}
                />
              </View>
            }
          </View>
        </TouchableOpacity>
      // there is a save button which can save the signature 
        <SignatureView
          ref={r => this._signatureView = r}
          rotateClockwise={!!true}
          onSave={this._onSave.bind(this)}
        />
      </View>
    );
  }
 
  // show the signature completed on the screen 
  _showSignatureView() {
    this._signatureView.show(true);
  }
 
  // save the signature 
  _onSave(result) {
    const base64String = `data:image/png;base64,${result.encoded}`;
    this.setState({data: base64String});

    this._signatureView.show(false);
  }
}

export default Signature;
