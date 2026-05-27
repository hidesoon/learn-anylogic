This folder has the customized models built for the AnyLogic webinar on using ChatGPT as a Java scripting aid. None of them are "functioning" simulation models, they simply have the results implemented by the code received from ChatGPT. 

A brief description is provided for each below; see the conversation logs document for more context.

---

**Dynamic Agent Placement - 1**: This model has 1 population of 'Location' agents whose animation icon is based on the 'tier' parameter value; this model tests the use of valid values (1-3) and an invalid value (4). ChatGPT wrote the conditions used for the icon visibility fields.

**Dynamic Agent Placement - 2**: This model has 3 populations of 'Location' agents, one for each valid tier value, whose positions are dynamically placed based on population size. The X position formulas were written by ChatGPT.

**DB View Test**: This is the start of a supply chain model, created as a demo of using Database Views to consolidate and reshape data from other tables into a format accepting by an agent population. It includes the initial (incorrect) DB query and the corrected query, both written by ChatGPT.

**USA States**: This model demonstrates calling a public API to dynamically generate agents, each representing a U.S. state with population size data for the specified year provided in the model's input. *All* of the code used for the API querying, including the import statements, were written by ChatGPT.