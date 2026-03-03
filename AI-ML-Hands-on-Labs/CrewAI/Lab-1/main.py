from crewai import Agent

# Define agents
venue_finder = Agent(
  role='Conference Venue Finder',
  goal='Find the best venue for the upcoming conference',
  backstory="You are an experienced event planner with a knack for finding the perfect venues.", 
            "Your expertise ensures that all conference requirements are met efficiently.",
  verbose = True
)

 from crewai import Task

# Define tasks
find_venue_task = Task(
    description=(
        "Conduct a thorough search to find the best venue for the upcoming "
        "conference. Consider factors such as capacity, location, amenities, "
        "and pricing. Use online resources and databases to gather comprehensive "
        "information."
    ),
    expected_output=(
        "A list of 5 potential venues with detailed information on capacity, "
        "location, amenities, pricing, and availability."
    ),
    agent=venue_finder
)