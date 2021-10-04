import React from "react";
import { View, Text } from "react-native";

import FancyDrawer from "../FancyDrawer";
import Header from "../Header";
import FancyBottomTab from "../FancyBottomTab";
import TweetBubble from "../TweetBubble";

class NavigationWraper extends React.Component {
  _handleShowDrawer = () => this.drawer._showProfile(0);
  _handleHeaderFade = i => this.header._fadeAvatar(i);

  _changeScreen_Details = screens =>
      this.props.navigation.navigate ("Details", {screen: screens})
      
  _changeScreen_Drawer = screens =>
      this.props.navigation.navigate ("Drawer", {screen: screens})

  _changeScreen_Main = screens =>
      this.props.navigation.navigate ("Main", {screen: screens})

  render() {
    return (
      <FancyDrawer
        fading={this._handleHeaderFade}
        ref={ref => (this.drawer = ref)}
        navigation={this._changeScreen_Drawer}
        profileName={"유저이름"}
        profileUserName={"유저이메일?정도"}
      >
        <Header
          ref={ref => (this.header = ref)}
          showProfile={this._handleShowDrawer}
          title={this.props.title}
          rightIcon={this.props.rightIcon}
          style={this.props.headerStyle}
        />
        {this.props.children}
        <TweetBubble
          message={this.props.selected !== 3}
          onBubblePress={
              this._changeScreen_Details.bind(this, "New Tweet")
          }
        />
        <FancyBottomTab
          selected={this.props.selected}
          navigation={this._changeScreen_Main}
        />
      </FancyDrawer>
    );
  }
}

export default NavigationWraper;