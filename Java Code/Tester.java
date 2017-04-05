import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.StreamTokenizer;

public class Tester {

	public static void main(String[] args) throws IOException {
		BTree real_dic_forward = new BTree();
		BTree real_dic_backward = new BTree();
		StreamTokenizer st = new StreamTokenizer(new BufferedReader(new FileReader("words.txt")));
		while (st.nextToken() != StreamTokenizer.TT_EOF)
			if (st.sval != null) {
				real_dic_forward.addWord(st.sval);
				real_dic_backward.addWord(backward(st.sval));
			}

		int total_words = 0;
		
		int real_words_100 = 0;
		int real_words_80 = 0;
		int real_words_60 = 0;

		
		BufferedReader br = new BufferedReader(new FileReader("test.txt"));
		String line;
		while((line = br.readLine()) != null){
			String[] parse = line.split(" ");
			String word = parse[0];
			int count = Integer.parseInt(parse[1]);
			
			int real_length = 0;
			int word_length = word.length();
			if (word != null && real_dic_forward.hasWord(word)){
				real_words_100+=count;
			}
			else {
				for (int i = 1; i < word_length; i++) {
					if (!real_dic_forward.hasWord(word.substring(0, i))) {
						real_length = i;
						break;
					}
				}
				String r = backward(word);
				for (int i = 1; i < word_length; i++) {
					if (!real_dic_backward.hasWord(r.substring(0, i))) {
						if (i > real_length)
							real_length = i;
						break;
					}
				}
			}
			double percent = ((double)real_length / (double)word_length) * 100;
			System.out.println(percent+" "+word+" "+real_length+" "+word_length+" "+count);
			if (percent >= 80)
				real_words_80+=count;
			else if (percent >= 60)
				real_words_60+=count;
			total_words+=count;
			
			
			
		}

		System.out.println("Real words 100 - " + real_words_100 + "\nReal words 80 - " + real_words_80 + "\nReal words 60 - " + real_words_60 + "\nTotal words - " + total_words);

		// try (BufferedReader br = new BufferedReader(new
		// FileReader("test.txt"))) {
		// String line;
		// String word;
		// Scanner c = new Scanner(line);
		// word = c.next();
		// while ((line = br.readLine()) != null) {
		// System.out.println(line);
		// }
		// } catch (IOException e) {
		// e.printStackTrace();
		// }

		// System.out.println("Dictionary by Melnik Boris");
		// Dictionary d = new Dictionary();
		// d.BSD();
		// d.words();

	}
	
	private static String backward(String s) {
		char[] mat = new char[s.length()];
		for (int i = 0; i < s.length(); i++) {
			mat[i] = s.charAt(s.length() - 1 - i);
		}
		return new String(mat);
	}

}