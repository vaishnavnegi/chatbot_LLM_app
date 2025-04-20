/// <reference types="nativewind/types" />
import { Text, View,SafeAreaView, ImageBackground  } from "react-native";
import { GestureHandlerRootView, TouchableOpacity } from "react-native-gesture-handler";
import {router} from "expo-router";


export default function Index() {

  return (
    <GestureHandlerRootView>
      <SafeAreaView className="w-full h-full">
      
        <ImageBackground 
          className="w-full h-full items-center"
          source={require('../assets/images/index_bg_image.png')}
        >
          <View className="flex h-[60%]" />
          <View className="flex w-[80%]">
            <Text 
            className="text-white text-2xl text-center font-[Sora-SemiBold]"
            >
              Best Coffee in town! You have to try it to believe it.
            </Text>

            <Text 
            className="pt-3 text-[#A2A2A2] text-center font-[Sora-Regular]" 
            >
            Are you ready to indulge in the cafe delight. Come join us!.
            </Text>
              <TouchableOpacity 
                className="bg-[#C57C3E] mt-10 py-3 rounded-lg items-center" 
                onPress = {() => router.push("/home")}
              >
                <Text className="text-xl text-white font-[Sora-SemiBold]">Let's Go</Text> 
              </TouchableOpacity> 
          </View>
        </ImageBackground>
      </SafeAreaView>
    </GestureHandlerRootView>
  );
}