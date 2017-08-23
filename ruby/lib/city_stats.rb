require_relative "aqicn-ruby-api-client"

class Station

  attr_reader :data

  def initialize(city_name)
    @city = city_name
    @@client ||= ApiClient.new
    @data = @@client.city_feed(@city)['data']
  end

  def name
    @data['name']
  end

  def url
    @data['city']['url']
  end

  def measurement_time
    @data['city']['time']
  end

  def pm_10
    pollution_data['pm10']['v']
  end

  private
  def pollution_data
    @data['iaqi']
  end
end

station = Station.new("Krakow")
p station.pm_10
