import React from "react";
import { View, Text, TouchableOpacity, Linking } from "react-native";
import { HeaderBackButton, NavigationActions } from "react-navigation";

class app extends React.Component {
  static navigationOptions = ({ navigation }) => ({
    headerLeft: (
      <HeaderBackButton
        onPress={() =>
          navigation.navigate(
            navigation.state.params.last,
            {},
            NavigationActions.navigate({ routeName: "Main" })
          )
        }
      />
    ),
    headerTitle: navigation.state.routeName
  });

  render() {
    return (
      <View
        style={{
          flex: 1,
          alignItems: "center",
          justifyContent: "center"
        }}
      >
        <Text style={{ fontSize: 16, fontWeight: "600" }}>
          {"미구현창"}
        </Text>

      </View>
    );
  }
}

export default app;
