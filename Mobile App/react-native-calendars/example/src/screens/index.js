import {Navigation} from 'react-native-navigation';

import MenuScreen from './menu';
import AgendaScreen from './agenda';
import Inventory from './inventory';
import ClassDetail from './classdetails';
import JsaList from './jsa';
import Signature from './signature';
import Attendee from './attendee';
import Note from './note';
import Feedback from './feedback';
import Qualification from './qualification';
import Comment from './comment';
import Status from './status';
import AddEquipment from './addequip';
/** The index file is generated by React Native to compile all screens together 
* Author: Yunpeng Wang
* Review By: Haonan Chen 
* Comment By: Haonan Chen
*/
AddEquipment
export function registerScreens() {
  Navigation.registerComponent('Menu', () => MenuScreen);
  Navigation.registerComponent('Agenda', () => AgendaScreen);
  Navigation.registerComponent('Inventory', () => Inventory);
  Navigation.registerComponent('ClassDetails', () => ClassDetail);
  Navigation.registerComponent('Jsa', () => JsaList);
  Navigation.registerComponent('Signature', () => Signature);
  Navigation.registerComponent('Attendee', () => Attendee);
  Navigation.registerComponent('Note', () => Note);
  Navigation.registerComponent('Feedback', () => Feedback);
  Navigation.registerComponent('Qualification', () => Qualification);
  Navigation.registerComponent('Status', () => Status);
  Navigation.registerComponent('Comment', () => Comment);
  Navigation.registerComponent('AddEquipment', () => AddEquipment);
}