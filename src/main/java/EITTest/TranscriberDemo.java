package EITTest;

import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import edu.cmu.sphinx.api.Configuration;
import edu.cmu.sphinx.api.SpeechResult;
import edu.cmu.sphinx.api.StreamSpeechRecognizer;
import edu.cmu.sphinx.util.TimeFrame;

public class TranscriberDemo {

	public static void main(String[] args) throws Exception {

		Configuration configuration = new Configuration();

		configuration
				.setAcousticModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us");
		configuration
				.setDictionaryPath("resource:/edu/cmu/sphinx/models/en-us/cmudict-en-us.dict");
		configuration
				.setLanguageModelPath("resource:/edu/cmu/sphinx/models/en-us/en-us.lm.bin");

		//StreamSpeechRecognizer recognizer = new StreamSpeechRecognizer(configuration);

		String path = "C:\\Users\\mikke\\IdeaProjects\\SpeechRecTest\\src\\main\\java\\EITTest\\test.wav";
		//InputStream stream = new FileInputStream(new File());

		StreamSpeechRecognizer recognizer = new StreamSpeechRecognizer(configuration);
		recognizer.startRecognition(new FileInputStream(path));
		SpeechResult result = recognizer.getResult();
		recognizer.stopRecognition();

		System.out.format("Hypothesis: %s\n", result.getHypothesis());

		//recognizer.startRecognition(stream, new TimeFrame(600));
		//recognizer.startRecognition(stream);
		//SpeechResult result;
		//while ((result = recognizer.getResult()) != null) {
	//		System.out.format("Hypothesis: %s\n", result.getHypothesis());
	//	}
		//recognizer.stopRecognition();
	}
}