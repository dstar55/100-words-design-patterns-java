package com.hundredwordsgof.interpreter;

/**
 * 
 * AbstractExpresion defines interface for interpretation. Interface must be
 * used by TerminalEpression and NonTerminalEpression.
 *
 */
public abstract class AbstractExpression {

  abstract void interpret(Context context);

}
