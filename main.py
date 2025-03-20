# main.py
from crew_setup import run_crew

def main():
    print("Welcome to the Natural Language SQL Query System")
    print("------------------------------------------------")
    
    while True:
        nl_query = input("\nEnter your question (or 'exit' to quit): ")
        
        if nl_query.lower() == 'exit':
            print("Exiting application. Goodbye!")
            break
            
        print("\nProcessing your query...\n")
        result = run_crew(nl_query)
        
        print("\n--- RESULT ---")
        print(result)
        print("---------------\n")

if __name__ == "__main__":
    main()