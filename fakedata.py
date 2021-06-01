from faker import Faker

faker = Faker()

# This class is uses the Faker Library to generate fake data. 
class FakeData:
    def __init__(self, num_records):
        self.num_records = num_records

    def gen_data(self):

        for i in range(self.num_records):
            yield {
                "Student Name": faker.name(),
                "Genedr": faker.random_element(
                    elements=("M", "F"),
                ),
                "CourseName": faker.random_element(
                    elements=("Math 240", "CS 400", "Stats 340", "Poli Sci 200"),
                ),
                "Grade": faker.random_element(
                    elements=("A", "AB", "B", "BC", "C", "D"),
                ),
                "IP_Address": faker.ipv4(),
                "TimeZone": faker.timezone(),
                "Avg_hours_per_day_online": faker.random_element(
                    elements=("1", "2", "3", "4", "5", ">5"),
                ),
                "lat": faker.latitude(),
                "lon": faker.longitude(),
            }
