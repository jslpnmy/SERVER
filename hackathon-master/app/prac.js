import React, {useState, useEffect} from 'react';
import { View , Text} from 'react-native';


const receiving = async (url) => {
  const data = await getMoviesFromApi(url)
  return data
}
const FixedDimensionsBasics = () => {
    const [dat, setCount] = useState(0);
    const [dat2, setDat] = useState(0);
    const url = 'https://reactnative.dev/movies.json'
    
    const getMoviesFromApi = (url) => {
        return fetch(url)
          .then((response) => {
              return response.json()})
          .then((json) => {
            return json;
          })
          .catch((error) => {
            console.error(error);
          });
      };
    useEffect(() => {
      receiving(url).then((d) => {
        console.log(d)
        setCount(d)
      })
    }, [])
    /*useEffect(() => {

        setCount(dataHandling())
    },[])*/
    
  return (
    <View>
        <Text>
     {JSON.stringify(dat)}
     </Text>
    </View>
  );
};

export default FixedDimensionsBasics;