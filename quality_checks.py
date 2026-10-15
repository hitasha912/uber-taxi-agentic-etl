from pyspark.sql.functions import *
from config import silver_path


def run_quality_checks(spark):
    df = spark.read.format("delta").load(silver_path)

    row_count = df.count()

    # Actual column names in the NCR ride bookings dataset
    required_columns = [
        "Date",
        "Time",
        "Booking_ID",
        "Booking_Status",
        "Customer_ID",
        "Vehicle_Type"
    ]

    null_counts = (
        df.select([
            count(when(col(c).isNull(), 1)).alias(c)
            for c in required_columns
        ])
        .first()
        .asDict()
    )

    # Validate Ride Distance
    invalid_distance = df.filter(
        (col("Ride_Distance").isNotNull()) &
        (col("Ride_Distance") < 0)
    ).count()

    # Validate Booking Value
    invalid_amount = df.filter(
        (col("Booking_Value").isNotNull()) &
        (col("Booking_Value") < 0)
    ).count()

    # Validate Driver Ratings
    invalid_ratings = df.filter(
        (col("Driver_Ratings").isNotNull()) &
        (~col("Driver_Ratings").between(1, 5))
    ).count()

    passed = (
        row_count > 0
        and all(value == 0 for value in null_counts.values())
        and invalid_distance == 0
        and invalid_amount == 0
        and invalid_ratings == 0
    )

    return {
        "status": "passed" if passed else "failed",
        "row_count": row_count,
        "null_counts": null_counts,
        "invalid_distance": invalid_distance,
        "invalid_amount": invalid_amount,
        "invalid_ratings": invalid_ratings
    }