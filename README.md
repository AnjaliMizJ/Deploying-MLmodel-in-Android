# Deploying-MLmodel-in-Android

-- After the process of training model and evaluation and getting the desired accuracy saved the model using tflite as "digit.tflite" in the specific location. 

<h2>In android</h2>

-- Create a project in android and creating an asset folder in the resource add saved tflite model into it. 
-- In the build.gradle(module.app) add:
                                       
                                                      
                                                       aaptOptions {
	                                                     noCompress "tflite"
	                                                     noCompress "lite"
	                                                    }

so that asset folder does not compress tflite model.
	
-- Also add  dependency of the keras in the project as :
							  
      							 Implementation  org.tensorflow:tensorflow-lite:+'
       							 implementation 'org.tensorflow:tensorflow-lite:1.13.1'
        
-- Add the below dependency to get the widget of painting frame in android (Since I used the model of digit recognizer so it is required to write freeely on the screen of mobile hence added this paint module):
        
               				 implementation 'com.nex3z:finger-paint-view:0.1.0
					 
After creating, the required layout to get image of handwritten number in android.Create a helper class as "Classifier.java" is initalizing the model name and the info about image like hieght, width, classnames etc. Then in the result activity performmed the prediction and the obtained result from the prediction was set in the ,ain activity.
        
Below is the vedio showing the final veiw of the result  of the project:
        
        
<p align="left"> <img src="https://komarev.com/ghpvc/?username=anjalimizj&label=Profile%20views&color=0e75b6&style=flat" alt="anjalimizj" /> </p>






