package com.hundredwordsgof.facade;

import java.util.List;

/**
 * 
 * Compiler has subclasses like Tokenizer, Parser, Generator, etc. Client which
 * use a compiler do not deal with subclasses in order to compile. Compiler
 * class represents a facade. Facade hides low-level functionality from client.
 *
 */
public class Compiler {

  public static int compile(String input) throws Exception {

    Parser parser = new Parser();
    List<String> tokens = Tokenizer.tokenize(input);
    Node expression = parser.parse(tokens);
    int result = Generator.generate(expression);

    return result;
  }
}
