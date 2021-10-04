import React from 'react';
import { Animated, Easing } from 'react-native';

import { Asset } from 'expo-asset';

import Navigator from './Navigate';

/*

import { Provider } from 'react-native-paper'
import { NavigationContainer } from '@react-navigation/native'
import { createStackNavigator } from '@react-navigation/stack'
import { theme } from './Login/core/theme'
import {
  StartScreen,
  LoginScreen,
  RegisterScreen,
  ResetPasswordScreen,
  Dashboard,
} from './Login/screens'

const Stack = createStackNavigator()

function Log() {
  return (
    <Provider theme={theme}>
      <NavigationContainer>
        <Stack.Navigator
          initialRouteName="StartScreen"
          screenOptions={{
            headerShown: false,
          }}
        >
          <Stack.Screen name="StartScreen" component={StartScreen} />
          <Stack.Screen name="LoginScreen" component={LoginScreen} />
          <Stack.Screen name="RegisterScreen" component={RegisterScreen} />
          <Stack.Screen name="Dashboard" component={<Navigator onNavigationStateChange={null} />} />
          <Stack.Screen
            name="ResetPasswordScreen"
            component={ResetPasswordScreen}
          />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
  )
}
*/
const Logo = require('../assets/image.png');

function cacheImages(images) {
  return images.map((image) => {
    if (typeof image === 'string') {
      return Image.prefetch(image);
    } else {
      return Asset.fromModule(image).downloadAsync();
    }
  });
}

/*class Loading extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      iconSize: new Animated.Value(80),
    };
  }

  _startAnimation = () =>
    Animated.timing(this.state.iconSize, {
      toValue: 2500,
      duration: 350,
      easing: Easing.back(0.4),
    }).start(() => this.props.animationEnd());

  render() {
    return (
      <Animated.View
        style={{
          flex: 1,
          alignItems: 'center',
          justifyContent: 'center',
          backgroundColor: '#1DA1F2',
        }}
      >
        <Animated.Image
          name={'logo'}
          style={{
            alignSelf: 'center',
            width: this.state.iconSize,
            height: this.state.iconSize,
          }}
          source={Logo}
        />
      </Animated.View>
    );
  }
}
*/
export default class RootComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isLoading: true,
    };
  }

  /*async _loadAssets() {
    const imageAssets = cacheImages([
      require('../assets/topMore.png'),
      require('../assets/thunder.png'),
      require('../assets/topStar.png'),
      require('../assets/topGear.png'),
      require('../assets/tweet.png'),
      require('../assets/message.png'),
      require('../assets/wizardsunite.png'),
      require('../assets/avatar/user1.jpg'),
      require('../assets/avatar/user2.jpg'),
      require('../assets/avatar/user3.jpg'),
      require('../assets/avatar/user4.jpg'),
      require('../assets/avatar/user5.jpg'),
      require('../assets/avatar/user6.jpg'),
    ]);
    await Promise.all([...imageAssets]).then(this.load._startAnimation);
  }

  componentDidMount = this._loadAssets;
*/
  render() {
    /*if (this.state.isLoading)
      return (
        <Loading
          ref={(ref) => (this.load = ref)}
          animationEnd={() => this.setState({ isLoading: false })}
        />
      );
*/
    return <Navigator onNavigationStateChange={null} />;
  }
}
