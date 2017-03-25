require_relative "aqicn-ruby-api-client"

class CityStats
  def initialize(city_name)
    @city = city_name
    @@client ||= ApiClient.new
    @data = @@client.city_feed(@city)
  end
end

cl = CityStats.new("Krakow")
cl = CityStats.new("Warsaw")
