Quiet Attic Films is a film production company based in London, England who specialize in making short information films and advertisements for television. They want you to design and implement a database that meets the requirements for their data. These requirements are specified in this scenario and the examples of paper documents kept by the company shown below. 
Quiet Attic Films organize their data around the concept of a ‘production’. A production is specified as being for a particular client; but note that a client might have more than one production at any time. A production will take place at one or more locations. A production will also use a number of, what are called, properties, which might be anything from an actual property like a building, to costumes or small items of any sort. It is important to keep a record of which properties are required at which location.
There should also be a record kept of the staff types that are assigned to productions

---------------------------------


In this project, I first analysed the given scenario to identify both the user requirements and the system requirements needed to design an effective database. I identified that users needed the ability to store, manage, update, delete, and retrieve information easily. The system also needed to maintain data accuracy, avoid duplication, and allow different types of data to be related to each other efficiently. Based on these requirements, I planned a database structure that would support organised data storage and efficient data retrieval.

After identifying the requirements, I created a conceptual database design using an Entity Relationship Diagram (ERD). In this diagram, I defined several entities representing the main components of the system such as customers, orders, products, payments, and employees. For each entity, I assigned a primary key to uniquely identify each record. I also defined the relationships between entities and clearly showed the cardinalities and participation of those relationships. For example, I defined that one customer can place many orders, while each order belongs to only one customer.

Once the ER model was completed, I converted the conceptual design into a logical database design using the relational database model. I created multiple interrelated tables based on the entities identified in the ER diagram. Each table contained appropriate attributes along with primary keys and foreign keys to maintain relationships between tables. Referential integrity was maintained by ensuring that foreign key values corresponded to valid primary key values in the related tables.

After developing the logical design, I evaluated whether the database structure was properly normalised. I checked the database against the normalisation rules to eliminate data redundancy and anomalies. The tables were structured so that they satisfied the First Normal Form by ensuring that all attributes contained atomic values. The design was further improved to satisfy the Second and Third Normal Forms by ensuring that non-key attributes were fully dependent on the primary key and that there were no transitive dependencies.

In addition to the database structure, I also designed simple interfaces that allow users to interact with the system. These interfaces included forms for inserting, updating, deleting, and viewing records in the database. I created wireframes to represent how users would input data and how information would be displayed. These interfaces were designed to be simple and user-friendly so that non-technical users could interact with the database system efficiently.

I evaluated the effectiveness of the ER diagram and logical database design based on the identified user and system requirements. The design ensured proper data organisation, reduced redundancy, maintained data integrity, and allowed efficient relationships between entities. The structure also supports future expansion and makes it easier to manage and retrieve information within the system.


------------------------------------


I developed the relational database system based on the ER diagram created in the previous activity. I used SQL Data Definition Language (DDL) statements to create the database tables and define their structures. Each table was created with appropriate attributes, primary keys, and foreign key constraints to ensure proper relationships between tables. This helped maintain referential integrity and ensured that related data remained consistent across the database.

To interact with the database, I used a suitable Integrated Development Environment (IDE) to create a simple interface that allows users to insert, update, and delete records. The interface was designed to make database operations easier for users without requiring them to write SQL queries manually. I provided evidence of this implementation through screenshots showing how the interface was used to manage the data stored in the database.

I also implemented basic security mechanisms within the database system to protect sensitive information and control access. Different levels of user permissions were considered to ensure that only authorised users could modify data while others could only view it. This helps maintain the security and integrity of the database system.

To demonstrate the functionality of the database, I used several SQL queries to retrieve and manipulate data. These included SQL statements such as SELECT, WHERE, UPDATE, BETWEEN, IN, GROUP BY, ORDER BY, and HAVING. These queries were used to extract meaningful information from the database, filter records based on conditions, update existing data, and organise results in a structured format.

I evaluated the overall effectiveness of the developed database system. The system successfully met the user and system requirements by providing an organised and secure way to store and manage data. The database structure ensures data consistency and integrity while allowing efficient retrieval of information. I also identified potential improvements such as implementing additional security features, improving indexing for faster queries, and enhancing the user interface for better usability.



-------------------------------------

I created a suitable test plan to verify that the developed database system meets the identified user and system requirements. The test plan included several test cases designed to evaluate different functionalities of the database such as inserting new records, updating existing records, deleting data, and retrieving information using queries. Each test case included the test description, input data, expected results, and the actual results obtained after performing the test.

I organised the test cases in a tabular format to clearly show the testing process. This made it easier to compare the expected results with the actual results generated by the system. Screenshots of the test results were also provided as evidence to demonstrate that the database system functions correctly. Through testing, I was able to confirm that the database handled operations accurately and maintained data integrity.

To further evaluate the system, I collected independent feedback from both non-technical users and developers. This feedback was gathered through simple questionnaires and informal interviews. Non-technical users provided insights on the usability and clarity of the interface, while developers evaluated the database structure, query efficiency, and system design.

Based on the feedback received, I analysed the strengths and weaknesses of the system and made a separate conclusion. The feedback helped identify areas where the interface could be improved and where additional features could be added to enhance usability and performance.


---------------------------------------

In this final activity, I produced both technical and user documentation for the completed database system. The technical documentation describes the database structure, system architecture, and how the database components interact with each other. This documentation helps developers understand how the system is built and how it can be maintained or extended in the future.

I also created user documentation that explains how end users can interact with the system. This includes instructions on how to add new records, update information, delete data, and retrieve reports from the database. The documentation was written in a clear and simple way so that users with limited technical knowledge can easily understand how to use the system.

Additionally, I created data flow diagrams (DFDs) to illustrate how data moves through the system from input to storage and output. Flowcharts were also included to describe the sequence of processes involved in performing various operations within the system. These diagrams help visualise the system’s workflow and make it easier to understand the overall functionality.

Finally, I evaluated the completed database system and suggested possible future enhancements. These improvements could include adding more advanced security features, improving system performance through indexing and optimisation, and expanding the database to support additional functionalities. These enhancements would help ensure the long-term effectiveness and scalability of the system.






