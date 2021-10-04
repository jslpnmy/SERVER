import React from "react";



import {
  ScrollView,
  TouchableHighlight,
  Text,
  StyleSheet,
  TouchableOpacity,
  Image, View
} from "react-native";

import { width, colors } from "../../utils";
import { homeFeed } from "../../mock";

import NavigationWraper from "../../components/NavigationWraper";
import Tweet from "../../components/Tweet";

import CardList from "react-native-card-animated-modal";
const now = new Date();
const CARDS = [
  {
    image: {
      uri:
        "https://cdn-icons-png.flaticon.com/128/739/739249.png"
    },
    height: 300,
    renderItem: ({ item, index }) => (
      <View>
        <Text>Customizable Content</Text>
      </View>
    )
  }
];


class Home extends React.Component {
  
  
  render() {

    return (
      <NavigationWraper
        navigation={this.props.navigation}
        selected={0}
        rightIcon={
          <TouchableOpacity style={{ padding: 5 }}>
            <Image
              style={{ height: 30, width: 30 }}
              source={require("../../../assets/favicon.png")}
              resizeMode={"contain"}
            />
          </TouchableOpacity>
        }
        title={
          <Text
            style={{
              fontWeight: "700",
              fontSize: 18,
              fontFamily: "HelveticaNeue-Bold"
            }}
          >
            {"Home"}
          </Text>
        }
      >
        <CardList
    listProps={{
      ListHeaderComponent: () => (
        <View style={{ padding: 16, paddingBottom: 0 }}>
          <Text
            style={{
              fontSize: 13,
              color: "rgba(0, 0, 0, 0.5)"
            }}
          >
            {now.toDateString()}
          </Text>
          <Text style={{ fontSize: 32, fontWeight: "bold" }}>게시물 제목</Text>
        </View>
      )
    }}
    data={CARDS}
    renderItem={({ item, index }) => {
      /* Render card per item */
      if (item.renderItem) return item.renderItem({ item, index });
 
      /* Default card when not specified */
      return (
        <View>
          <Text>Default Content</Text>
        </View>
      );
    }}
    renderDetails={({ item, index }) => (
      /* You can also provide custom content per item */
      <View style={{ paddingVertical: 30, paddingHorizontal: 16 }}>
        <Text style={{ color: "rgba(0, 0, 0, 0.7)", fontSize: 18 }}>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </Text>
      </View>
    )}
  />


      </NavigationWraper>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    width: width,
    backgroundColor: colors.exexlight_gray,
    fontWeight: "700",
              fontSize: 18,
              fontFamily: "HelveticaNeue-Bold"
  }
});

export default Home;

