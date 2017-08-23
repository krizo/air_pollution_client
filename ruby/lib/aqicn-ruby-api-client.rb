require "httparty"

class ApiClient
  include HTTParty

  base_uri "https://api.waqi.info/"

  def initialize
    @token = '86b48480160bd9c5f267b004e13b1fe27b75d7e7'
  end

  def city_feed(city)
    handle_response(self.class.get("/feed/#{city}/?token=#{@token}"))
  end

  private
  def handle_response(response)
    case response.code.to_i
    when 200, 201, 300
      response
    else
      raise "Error request: #{response}"
    end
  end
end
