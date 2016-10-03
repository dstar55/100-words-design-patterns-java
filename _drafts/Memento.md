---
layout: page
title: Memento
permalink: /Memento/
tag: pattern
---

Memento


# Story 

Helps to restore an object’s state to it previous state.

Transactions are operations on the database that occur in an atomic, consistent, durable, and isolated fashion. 
A transaction can contain multiple operations on the database; each operation can succeed or fail, however a transaction guarantees that if all operations succeed, 
the transaction would commit and would be final. 
And if any operation fails, then the transaction would fail and all operations would rollback and leave the database as if nothing has happened.

This mechanism of rolling back uses the memento design pattern. 




