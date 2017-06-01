=begin
Ivo needs a lift to the center. If someone finishes work at 4.30 and if someone has car, Ivo will fget lift to the city center.
=end

friend_off = false #someone who finishes at 4.30 pm
friend_with_car = true # someone who has car

if friend_off && friend_with_car
    puts "Ivo is going to the city center by car!"
elsif friend_off || friend_with_car
    puts "Ivo will have to ask other friends!"
else
    puts "Ivo is not going to city center. At lease not by car!"
end
