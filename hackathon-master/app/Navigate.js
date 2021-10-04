import React from "react";

import { StatusBar } from "react-native";
/*
import {
  createAppContainer,
  createSwitchNavigator,
  createStackNavigator
} from "react-navigation";*/



//login
import { theme } from './Login/core/theme'
import { Provider } from 'react-native-paper'
import {
  StartScreen,
  LoginScreen,
  RegisterScreen,
  ResetPasswordScreen,
  Dashboard,
} from './Login/screens'
//login


import Home from "./screens/Home";
import Search from "./screens/Search";
import Notification from "./screens/Notification";
import Message from "./screens/Message";

import UnderConstruction from "./screens/UnderConstruction";
import TweetButton from "./screens/TweetButton"


import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import { createDrawerNavigator } from '@react-navigation/drawer';

const Stack = createStackNavigator()
const Drawer = createDrawerNavigator();

function Logins() {
  return (
    <Provider theme={theme}>
        <Stack.Navigator
          initialRouteName="StartScreen"
          screenOptions={{
            headerShown: false,
          }}
        >
          <Stack.Screen name="StartScreen" component={StartScreen} />
          <Stack.Screen name="LoginScreen" component={LoginScreen} />
          <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
          <Stack.Screen name="Dashboard" component={Dashboard} />
          <Stack.Screen
            name="ResetPasswordScreen"
            component={ResetPasswordScreen}
          />
        </Stack.Navigator>
    </Provider>
  )
}
function Drawers() {
  return (
    <Drawer.Navigator>
          <Drawer.Screen name="Profile" component={UnderConstruction} />
          <Drawer.Screen name="Popular" component={UnderConstruction} />
          <Drawer.Screen name="Saved" component={UnderConstruction} />
          <Drawer.Screen name="Discover" component={UnderConstruction} />
          <Drawer.Screen name="Configuration" component={UnderConstruction} />
          <Drawer.Screen name="Help Center" component={UnderConstruction} />
        </Drawer.Navigator>
  )
}

function Main() {
  return (
    <Stack.Navigator initialRouteName="Home">
          <Stack.Screen name="Home" component={Home} />
          <Stack.Screen name="Search" component={Search} />
          <Stack.Screen name="Notification" component={Notification} />
          <Stack.Screen name="Message" component={Message} />
        </Stack.Navigator>
  )
}

function Detail() {
  return (
    <Stack.Navigator>
          <Stack.Screen name="Tweet" component={UnderConstruction} />
          <Stack.Screen name="New Tweet" component={TweetButton} />
          <Stack.Screen name="New Message" component={UnderConstruction} />
          <Stack.Screen name="DynamicTitle" component={UnderConstruction} />
        </Stack.Navigator> 
  )
}

export default function App() {
  return (
      <NavigationContainer>
        <Stack.Navigator
         initialRouteName="Logins"
         screenOptions={{
          headerMode: 'none',
        }}
          > 
          <Stack.Screen name="Logins" component={Logins} />
          <Stack.Screen name="Main" component={Main} />
          <Stack.Screen name="Drawer" component={Drawers} />
          <Stack.Screen name="Details" component={Detail} />
        </Stack.Navigator> 
      </NavigationContainer>
  )
}

/*
export default createAppContainer(
  createSwitchNavigator(
    {
      Main: createSwitchNavigator(
        {
          Home: Home,
          Search: Search,
          Notification: Notification,
          Message: Message
        },
        { initialRouteName: "Home" }
      ),
      Drawer: createStackNavigator({
        Profile: UnderConstruction,
        Popular: UnderConstruction,
        Saved: UnderConstruction,
        Discover: UnderConstruction,
        Configuration: UnderConstruction,
        "Help Center": UnderConstruction
      }),
      Details: createStackNavigator({
        Tweet: UnderConstruction,
        "New Tweet": TweetButton,
        "New Message": UnderConstruction,
        DynamicTitle: UnderConstruction
      })
    },
    {
      initialRouteName: "Main",
      headerMode: "none",
      cardStyle: { paddingTop: StatusBar.currentHeight }
    }
  )
);

*/